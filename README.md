# Dependency Graph Checker

Validate a small dependency graph, calculate a deterministic topological order and depth, or return an explicit cycle path.

```bash
python3 app.py examples/services.json --dot outputs/services.dot
python3 app.py examples/cycle.json
```

The DOT file can be rendered by Graphviz if you already use it; Graphviz is not required. Every referenced dependency must be declared.

## Tests
`python3 -m unittest discover -s tests -v`

## License
MIT. Maintainer: Shikhar Singh.
