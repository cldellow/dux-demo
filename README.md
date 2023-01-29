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
datasette publish fly cooking.db superuser.db --app="dux-demo" --install datasette-block-robots --install datasette-ui-extras --metadata metadata.json --plugins-dir plugins --setting facet_time_limit_ms 1000 --setting sql_time_limit_ms 1000 --setting default_cache_ttl 300 --branch 1.0a2
```
