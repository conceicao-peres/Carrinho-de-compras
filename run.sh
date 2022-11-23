#!/bin/bash

exec uvicorn aplicacao:main  --host 0.0.0.0 --factory