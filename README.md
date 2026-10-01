# My Project
Learning Git step by step.

## GitHub Actions examples

| Workflow | Shows |
|---|---|
| `ci.yml` | The minimal workflow: checkout + run commands |
| `python-ci.yml` | Lint (ruff) then test (pytest) on a Python version matrix, using a composite action |
| `matrix.yml` | OS × version matrix with `include`/`exclude`, `fail-fast`, `continue-on-error` |
| `env-and-outputs.yml` | `env` at workflow/job/step scope, `GITHUB_ENV`, step & job outputs, secrets, job summary |
| `conditionals.yml` | `needs`, `if:`, `failure()` / `always()`, event-specific jobs |
| `artifacts.yml` | `actions/cache`, uploading and downloading artifacts between jobs |
| `manual.yml` | `workflow_dispatch` with string / choice / boolean inputs |
| `scheduled.yml` | Cron `schedule` trigger |
| `reusable-greet.yml` + `call-reusable.yml` | Reusable workflows (`workflow_call`) with inputs, secrets, outputs |
| `paths-and-concurrency.yml` | `paths` filters, `concurrency` with cancel-in-progress, `timeout-minutes` |
| `release.yml` | Tag-triggered release with `permissions` and the `gh` CLI |

The composite action lives in `.github/actions/setup-project/action.yml`.

### Running locally

```sh
pip install -r requirements-dev.txt && pytest      # run the tests
act -l                                             # list all jobs
act push -W .github/workflows/python-ci.yml        # run one workflow
act workflow_dispatch -W .github/workflows/manual.yml --input name=git
act -s MY_SECRET=shh -W .github/workflows/env-and-outputs.yml
```

The repo's `.actrc` makes `act` use the `catthehacker/ubuntu:act-latest` image, because
`actions/setup-python` doesn't work on slim `node:*` images.
