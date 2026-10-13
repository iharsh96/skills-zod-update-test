# Commit types

| Type | Use it for |
|---|---|
| `feat` | A new feature for users |
| `fix` | A bug fix |
| `docs` | Documentation only |
| `style` | Formatting with no behaviour change |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf` | A performance improvement |
| `test` | Adding or fixing tests |
| `build` | Build system or dependencies |
| `ci` | CI configuration |
| `chore` | Other maintenance that doesn't touch source or tests |
| `revert` | Reverts an earlier commit |

## Breaking changes

Add `!` after the type or scope (`feat(api)!: drop v1 endpoints`) and explain the change in a `BREAKING CHANGE:` footer.

## Source

Based on the Conventional Commits 1.0.0 specification: https://www.conventionalcommits.org/en/v1.0.0/
