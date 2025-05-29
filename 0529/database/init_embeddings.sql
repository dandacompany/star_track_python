-- 1-1. 테이블
CREATE TABLE IF NOT EXISTS embeddings (
  id         BIGSERIAL PRIMARY KEY,
  content    TEXT,
  embedding  VECTOR(384),         -- MiniLM-L6-v2 384-d
  created_at TIMESTAMPTZ DEFAULT timezone('utc', now())
);

-- 1-2. HNSW 인덱스 (코사인 거리)
CREATE INDEX IF NOT EXISTS embeddings_hnsw_cos
  ON embeddings
  USING hnsw (embedding vector_cosine_ops);

-- 1-3. 최근접 검색 RPC
CREATE OR REPLACE FUNCTION match_embeddings (
  query_embedding  VECTOR(384),
  match_threshold  REAL    DEFAULT 0.78,
  match_count      INTEGER DEFAULT 5
)
RETURNS TABLE (
  id         BIGINT,
  content    TEXT,
  similarity REAL
)
LANGUAGE sql STABLE AS $$
  SELECT id,
         content,
         1 - (embedding <=> query_embedding) AS similarity      -- cosine
  FROM   embeddings
  WHERE  embedding <=> query_embedding < 1 - match_threshold
  ORDER  BY embedding <=> query_embedding
  LIMIT  match_count;
$$;
