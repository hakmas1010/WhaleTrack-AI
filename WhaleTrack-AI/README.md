# WhaleTrack-AI (Placeholder)

⚠️ Placeholder repo, real code private.

## Project Goal
Help investors track big whales & avoid rug pulls.

## Problem It Solves
Market scams, fake hype, investor losses.

## Vision
Provide AI-powered insights, verified by professionals, released to users safely.

## Current Status
MVP in development.

## Demo (Interactive CLI)
This placeholder includes a simple interactive CLI that demonstrates the vision:

- Track big whales across stocks & crypto (simulated events)
- View market movement and a basic forecast (placeholder)
- Receive financial freedom guidance tips (AI-driven in real MVP)

Launch the CLI and explore the menu to see how the real product will feel.

## How to Run (Windows PowerShell)
```
./run.ps1
```
This will create a virtual environment (if needed) and run `python -m src.main`.

## Notes
- No real market connections or models are included in this placeholder.
- Real code, signals, and guidance models will be added at MVP.

## Configuration
Settings file: `settings.json`

```
{
  "sources": { "crypto": true, "stocks": true },
  "thresholds": { "crypto_tx_usd": 1000000, "stock_block_trade_usd": 5000000 },
  "alerts": { "write_to_file": true, "file_path": "data/alerts.log" }
}
```

## Logs
Alerts are appended to `data/alerts.log` when `alerts.write_to_file` is enabled.
