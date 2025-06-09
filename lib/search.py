from elasticsearch import Elasticsearch
from elasticsearch import Elasticsearch

def analyze_morph(
    text,
    analyzer=None,
    tokenizer=None,
    filters=None,
    explain=False,
    decompound_mode=None,
    user_dictionary_rules=None,
    index=None,
    hosts="http://localhost:9200"
):
    """
    Elasticsearch Nori 형태소 분석 함수

    Parameters:
        text (str or list): 분석할 문장 또는 문장 리스트
        analyzer (str): 사용할 analyzer 이름 (예: 'nori' 또는 'my_nori_analyzer')
        tokenizer (str): 사용할 tokenizer 이름 (예: 'nori_tokenizer')
        filters (list): 사용할 filter 리스트
        explain (bool): 형태소 품사 정보 등 상세 결과 포함 여부
        decompound_mode (str): 'none', 'discard', 'mixed' 중 선택
        user_dictionary_rules (list): 사용자 정의 단어 리스트
        index (str): 인덱스명 (없으면 _analyze 엔드포인트 사용)
        hosts (str or list): Elasticsearch 호스트

    Returns:
        dict: 분석 결과(JSON)
    """
    es = Elasticsearch(hosts)
    body = {"text": text}

    if analyzer:
        body["analyzer"] = analyzer
    if tokenizer:
        body["tokenizer"] = tokenizer
    if filters:
        body["filter"] = filters
    if explain:
        body["explain"] = True
    if decompound_mode or user_dictionary_rules:
        # tokenizer를 dict로 세부 옵션 지정
        body["tokenizer"] = {"type": "nori_tokenizer"}
        if decompound_mode:
            body["tokenizer"]["decompound_mode"] = decompound_mode
        if user_dictionary_rules:
            body["tokenizer"]["user_dictionary_rules"] = user_dictionary_rules

    if index:
        result = es.indices.analyze(index=index, body=body)
    else:
        result = es.indices.analyze(body=body)
    return result


def create_index(
    index_name,
    settings=None,
    mappings=None,
    hosts="http://localhost:9200"
):
    """
    Elasticsearch 인덱스 생성 함수 (elasticsearch-py 기반)

    Parameters:
        index_name (str): 생성할 인덱스명 (소문자)
        settings (dict): 인덱스 설정 (예: 샤드, 레플리카, 분석기 등)
        mappings (dict): 인덱스 매핑 (필드 타입 등)
        hosts (str or list): Elasticsearch 호스트

    Returns:
        dict: 생성 결과(JSON)
    """
    es = Elasticsearch(hosts)
    # 이미 인덱스가 있으면 삭제(옵션)
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
    body = {}
    if settings:
        body["settings"] = settings
    if mappings:
        body["mappings"] = mappings
    return es.indices.create(index=index_name, body=body)

DEFAULT_SETTINGS = {
    "analysis": {
        "analyzer": {
            "nori_analyzer": {
                "type": "custom",
                "tokenizer": "nori_tokenizer"
            }
        }
    }
}
DEFAULT_MAPPINGS = {
    "properties": {
        "title": {"type": "text", "analyzer": "nori_analyzer"},
        "content": {"type": "text", "analyzer": "nori_analyzer"}
    }
}