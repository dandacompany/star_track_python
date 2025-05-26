from mcp.server.fastmcp import FastMCP
import pandas as pd
import os
import tempfile
import json
from typing import List, Optional, Dict, Any
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import argparse

mcp = FastMCP(
    name="kaggle-mcp-server",
    instructions="Kaggle API를 활용한 데이터셋 조회, 다운로드 및 분석을 수행하는 MCP 서버"
)

@mcp.tool('authenticate', "Kaggle API 인증")
async def authenticate(
    kaggle_username: str,
    kaggle_key: str
) -> dict:
    """Kaggle API 인증을 수행합니다"""
    # 환경 변수 설정
    os.environ['KAGGLE_USERNAME'] = kaggle_username
    os.environ['KAGGLE_KEY'] = kaggle_key
    
    try:
        # API 인증 시도
        api = KaggleApi()
        api.authenticate()
        return {
            "success": True,
            "message": "Kaggle API 인증에 성공했습니다."
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Kaggle API 인증 실패: {str(e)}"
        }

@mcp.tool('list_datasets', "Kaggle 데이터셋 목록 조회")
async def list_datasets(
    search_query: str = "",
    max_results: int = 10,
    sort_by: str = "relevance"
) -> dict:
    """검색 쿼리에 맞는 Kaggle 데이터셋 목록을 조회합니다"""
    try:
        api = KaggleApi()
        api.authenticate()
        
        # 데이터셋 검색
        datasets = api.dataset_list(search=search_query, sort_by=sort_by)
        
        result = []
        count = 0
        for dataset in datasets:
            if count >= max_results:
                break
            dataset_info = {
                "ref": dataset.ref,  # owner/dataset-name 형식
                "title": dataset.title,
            }
            
            # 안전하게 속성 추가
            if hasattr(dataset, 'size'):
                dataset_info["size"] = dataset.size
            if hasattr(dataset, 'lastUpdated'):
                dataset_info["last_updated"] = str(dataset.lastUpdated)
            if hasattr(dataset, 'downloadCount'):
                dataset_info["download_count"] = dataset.downloadCount
            if hasattr(dataset, 'voteCount'):
                dataset_info["vote_count"] = dataset.voteCount
            if hasattr(dataset, 'tags'):
                dataset_info["tags"] = dataset.tags
            if hasattr(dataset, 'usabilityRating'):
                dataset_info["usability_rating"] = dataset.usabilityRating
            
            result.append(dataset_info)
            count += 1
        
        return {
            "success": True,
            "count": len(result),
            "datasets": result
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"데이터셋 목록 조회 실패: {str(e)}"
        }
@mcp.tool('dataset_info', "Kaggle 데이터셋 상세 정보 조회")
async def dataset_info(
    dataset_ref: str  # owner/dataset-name 형식
) -> dict:
    """특정 Kaggle 데이터셋의 상세 정보를 조회합니다"""
    try:
        api = KaggleApi()
        api.authenticate()
        
        # 데이터셋 상세 정보 조회 (dataset_view 대신 dataset_list_files를 사용하여 정보 얻기)
        owner, dataset_name = dataset_ref.split('/')
        datasets = api.dataset_list(search=dataset_name, owner=owner)
        
        # 일치하는 데이터셋 찾기
        dataset = None
        for ds in datasets:
            if ds.ref == dataset_ref:
                dataset = ds
                break
                
        if not dataset:
            return {
                "success": False,
                "message": f"데이터셋을 찾을 수 없습니다: {dataset_ref}"
            }
        
        # 파일 목록 가져오기
        files = api.dataset_list_files(dataset_ref).files
        file_list = [{'name': f.name, 'size': f.size} for f in files]
        
        # 데이터셋 정보 구성
        dataset_info = {
            "ref": dataset_ref,
            "title": dataset.title,
            "files": file_list
        }
        
        # 안전하게 속성 추가
        if hasattr(dataset, 'description'):
            dataset_info["description"] = dataset.description
        if hasattr(dataset, 'size'):
            dataset_info["size"] = dataset.size
        if hasattr(dataset, 'lastUpdated'):
            dataset_info["last_updated"] = str(dataset.lastUpdated)
        if hasattr(dataset, 'downloadCount'):
            dataset_info["download_count"] = dataset.downloadCount
        if hasattr(dataset, 'voteCount'):
            dataset_info["vote_count"] = dataset.voteCount
        if hasattr(dataset, 'tags'):
            dataset_info["tags"] = dataset.tags
        if hasattr(dataset, 'license'):
            dataset_info["license"] = dataset.license
        
        return {
            "success": True,
            "dataset": dataset_info
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"데이터셋 정보 조회 실패: {str(e)}"
        }

@mcp.tool('download_dataset', "Kaggle 데이터셋 다운로드")
async def download_dataset(
    dataset_ref: str,  # owner/dataset-name 형식
    output_path: str = None,
    unzip: bool = True
) -> dict:
    """Kaggle 데이터셋을 다운로드합니다"""
    try:
        api = KaggleApi()
        api.authenticate()
        
        # 출력 경로 설정
        if output_path is None:
            output_path = tempfile.mkdtemp()
        
        # 데이터셋 다운로드
        api.dataset_download_files(dataset_ref, path=output_path, unzip=unzip)
        
        # 다운로드된 파일 목록
        file_list = []
        for root, dirs, files in os.walk(output_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                file_list.append({
                    "name": file,
                    "path": file_path,
                    "size": file_size
                })
        
        return {
            "success": True,
            "message": f"데이터셋 '{dataset_ref}'가 성공적으로 다운로드되었습니다.",
            "output_path": output_path,
            "files": file_list
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"데이터셋 다운로드 실패: {str(e)}"
        }

@mcp.tool('preview_dataset', "Kaggle 데이터셋 미리보기")
async def preview_dataset(
    dataset_ref: str,  # owner/dataset-name 형식
    file_name: str,
    rows: int = 10
) -> dict:
    """데이터셋의 특정 파일을 미리봅니다 (CSV 또는 다른 표 형식 파일을 지원)"""
    try:
        api = KaggleApi()
        api.authenticate()
        
        # 임시 디렉토리에 다운로드
        temp_dir = tempfile.mkdtemp()
        api.dataset_download_file(dataset_ref, file_name, path=temp_dir)
        
        # 파일 경로
        file_path = ""
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file == file_name or file == f"{file_name}.zip":
                    file_path = os.path.join(root, file)
                    break
        
        # 파일 확장자에 따라 처리
        if file_path.endswith('.zip'):
            import zipfile
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
                file_path = os.path.join(temp_dir, file_name)
        
        # 파일 타입에 따른 처리
        if file_name.endswith('.csv'):
            df = pd.read_csv(file_path)
            preview_data = df.head(rows).to_dict()
            columns = df.columns.tolist()
            dtypes = df.dtypes.astype(str).to_dict()
            shape = df.shape
        elif file_name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
            preview_data = df.head(rows).to_dict()
            columns = df.columns.tolist()
            dtypes = df.dtypes.astype(str).to_dict()
            shape = df.shape
        else:
            # 텍스트 파일로 가정하고 처리
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f.readlines()[:rows]]
            preview_data = {"lines": lines}
            columns = []
            dtypes = {}
            shape = (len(lines), 0)
        
        return {
            "success": True,
            "file_name": file_name,
            "preview": preview_data,
            "columns": columns if hasattr(locals(), 'columns') else [],
            "dtypes": dtypes if hasattr(locals(), 'dtypes') else {},
            "shape": shape if hasattr(locals(), 'shape') else (0, 0)
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"데이터셋 미리보기 실패: {str(e)}"
        }

@mcp.tool('list_competitions', "Kaggle 대회 목록 조회")
async def list_competitions(
    search_query: str = "",
    category: str = "all",
    max_results: int = 10
) -> dict:
    """Kaggle 대회 목록을 조회합니다"""
    try:
        api = KaggleApi()
        api.authenticate()
        
        # 대회 검색
        competitions = api.competitions_list(search=search_query, category=category, page_size=max_results)
        
        result = []
        for competition in competitions:
            result.append({
                "ref": competition.ref,
                "title": competition.title,
                "url": competition.url,
                "deadline": str(competition.deadline),
                "category": competition.category,
                "reward": competition.reward,
                "team_count": competition.teamCount
            })
        
        return {
            "success": True,
            "count": len(result),
            "competitions": result
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"대회 목록 조회 실패: {str(e)}"
        }

@mcp.tool('analyze_dataset', "다운로드된 CSV 데이터셋 분석")
async def analyze_dataset(
    file_path: str,
    delimiter: str = ",",
    sample_size: int = 5
) -> dict:
    """다운로드된 CSV 파일을 분석합니다"""
    try:
        # CSV 파일 로드
        df = pd.read_csv(file_path, delimiter=delimiter)
        
        # 기본 통계
        stats = df.describe(include='all').to_dict()
        
        # 결측값 정보
        missing_values = df.isnull().sum().to_dict()
        missing_percent = (df.isnull().mean() * 100).to_dict()
        
        # 데이터 타입 정보
        dtypes = df.dtypes.astype(str).to_dict()
        
        # 상관관계 (수치형 변수만)
        try:
            corr = df.corr(numeric_only=True).to_dict()
        except:
            corr = {"message": "상관관계를 계산할 수 없습니다."}
        
        return {
            "success": True,
            "file_info": {
                "path": file_path,
                "columns": df.columns.tolist(),
                "shape": df.shape,
                "sample": df.head(sample_size).to_dict(),
                "dtypes": dtypes
            },
            "statistics": stats,
            "missing_values": missing_values,
            "missing_percent": missing_percent,
            "correlation": corr
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"데이터셋 분석 실패: {str(e)}"
        }

if __name__ == "__main__":
    # 명령줄 인수 파싱 추가
    parser = argparse.ArgumentParser(description="Kaggle MCP 서버")
    parser.add_argument("--username", help="Kaggle API 사용자 이름")
    parser.add_argument("--key", help="Kaggle API 키")
    args = parser.parse_args()

    # 인증 정보가 제공된 경우 환경 변수 설정
    if args.username and args.key:
        os.environ['KAGGLE_USERNAME'] = args.username
        os.environ['KAGGLE_KEY'] = args.key
        print(f"Kaggle API 인증 정보가 설정되었습니다. 사용자: {args.username}")
    else:
        print("Kaggle API 인증 정보가 제공되지 않았습니다. 필요시 authenticate 도구를 사용하세요.")

    print("Kaggle MCP 서버 시작...")
    mcp.run(
        transport="stdio"
    )
