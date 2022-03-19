# https://pgtune.leopard.in.ua/#/

# postgres version
FROM postgres:14.1

# postgres password & user
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

# postgres environment
ENV max_connections = 200
ENV shared_buffers = 8GB
ENV effective_cache_size = 24GB
ENV maintenance_work_mem = 2GB
ENV checkpoint_completion_target = 0.9
ENV wal_buffers = 16MB
ENV default_statistics_target = 100
ENV random_page_cost = 1.1
ENV effective_io_concurrency = 200
ENV work_mem = 20971kB
ENV min_wal_size = 1GB
ENV max_wal_size = 4GB

# postgres Timezone 을 맞추어 DB upload 시 생길수 있는 error 방지
ENV TZ = "Asia/seoul"

# Port
EXPOSE 5432

