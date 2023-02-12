# Clean environment for demo

This publishes a plugin with [datasette-ui-extras](https://github.com/cldellow/datasette-ui-extras/) to https://dux-demo.fly.dev/

```bash
python3 -mvenv venv
. venv/bin/activate
pip install datasette
datasette install datasette-ui-extras datasette-publish-fly
cp ~/src/stackexchange-to-sqlite/stack.db cooking.db
sqlite-utils enable-fts cooking.db posts title body
sqlite-utils enable-fts superuser.db posts title body
datasette publish fly --app="dux" --install datasette-auth-github --install datasette-block-robots --install datasette-ui-extras --install datasette-cluster-map --install datasette-parquet --install datasette-current-actor --metadata metadata.json --plugins-dir plugins --setting facet_time_limit_ms 1000 --setting sql_time_limit_ms 1000 --setting default_cache_ttl 300 --setting truncate_cells_html 500 --setting force_https_urls 1 --branch 1.0a2 --plugin-secret datasette-auth-github client_secret "$(cat .github-client-secret)"
```
