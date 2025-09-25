from brokers import exness, deriv
from strategies import scalping, ict, turtle_soup

def main():
    print("=== Zark Trading Bot ===")
    # Example: pick broker and strategy
    broker = exness  # or deriv
    strategy = scalping  # or ict, turtle_soup
    
    # Connect to broker
    print("Connecting to broker...")
    broker.connect()
    
    # Run strategy loop (stub)
    print(f"Starting {strategy.__name__} strategy...")
    for signal in strategy.generate_signals():
        print(f"Signal: {signal}")
        # Place order logic (stub)
        # broker.place_order(signal)

if __name__ == "__main__":
    main()