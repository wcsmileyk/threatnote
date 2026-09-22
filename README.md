![img](https://i.imgur.com/xqc8bGL.png)

## Getting Started
Check out the docs at https://docs.threatnote.io/ to get started!

## Quick Start
First you'll want to clone the threatnote.io repo
```
$ git clone git@github.com:brianwarehime/threatnote.git
$ cd threatnote/threatnote
$ cp env_example env
$ vi env (change the secret key, add any enrichment API keys)
$ docker compose up -d --build
```
Then browse to http://localhost:5000.

This will launch the following containers:

- `threatnote`: the Flask app served by gunicorn on port 5000
- `worker`: an rq worker listening on the `enricher` queue to run enrichment jobs
- `redis`: the Redis server backing the job queue

The SQLite database lives in `./db` on the host and is shared by the app and the worker.

To stop threatnote.io, just run:
`$ docker compose down`

To login, use admin@threatnote.io and admin as your credentials, then change the password under Settings.

Passwords stored by older versions of threatnote are still accepted and are upgraded to a modern hash the next time each user logs in.

For a general overview of the product, check out https://threatnote.io
