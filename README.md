# Clean environment for demo

This publishes a plugin with [datasette-ui-extras](https://github.com/cldellow/datasette-ui-extras/) to https://dux-demo.fly.dev/

```bash
python3 -mvenv venv
. venv/bin/activate
pip install datasette
datasette install datasette-ui-extras datasette-publish-fly
cp ~/src/stackexchange-to-sqlite/stack.db cooking.db
datasette publish fly cooking.db --app="dux-demo"--install datasette-ui-extras --metadata metadata.json
```
