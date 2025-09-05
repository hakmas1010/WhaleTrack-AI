# Placeholder – real implementation private.
from src.core.tracker import Tracker
from src.ai.forecast import forecast_market
from src.security.alerts import AlertManager
import time
import sys


def track_big_whales():
    print("\n[track] scanning on-chain and market feeds for large moves... (placeholder)")
    time.sleep(0.5)
    print("found: wallet 0xABC... moved 12,500 ETH to exchange (placeholder)")
    print("found: fund XYZ bought 150k shares of ACME (placeholder)")


def market_movement():
    print("\n[movement] computing market momentum and volatility... (placeholder)")
    time.sleep(0.5)
    _ = forecast_market(None)
    print("signal: moderate uptrend; watch for rug-pull indicators in small-cap tokens (placeholder)")


def financial_guidance():
    print("\n[guidance] personalized financial freedom tips (placeholder)")
    time.sleep(0.3)
    tips = [
        "automate savings: pay yourself first",
        "diversify core holdings; avoid overexposure",
        "risk budget: size positions to sleep well",
        "focus on long-term compounding",
    ]
    for t in tips:
        print(" -", t)


def main():
    print("[WhaleTrack-AI] Starting... (placeholder)")
    t = Tracker()
    t.run()
    AlertManager().send_alert("system initialized (placeholder)")

    # Non-interactive or demo mode fallback
    if (len(sys.argv) > 1 and sys.argv[1] == "--demo") or not sys.stdin.isatty():
        print("[demo] non-interactive mode detected; running scripted sequence...")
        track_big_whales()
        market_movement()
        financial_guidance()
        print("[demo] done.")
        return

    while True:
        print("\nSelect an option:")
        print("  1) Track big whales (stocks & crypto)")
        print("  2) Market movement & forecast")
        print("  3) Financial freedom guidance (AI)")
        print("  0) Exit")
        choice = input("> ").strip()
        if choice == "1":
            track_big_whales()
        elif choice == "2":
            market_movement()
        elif choice == "3":
            financial_guidance()
        elif choice == "0":
            break
        else:
            print("Unknown option. Try again.")


if __name__ == "__main__":
    main()
