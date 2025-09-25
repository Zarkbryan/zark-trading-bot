def calculate_position_size(balance, risk_per_trade, stop_loss_pips, pip_value):
    risk_amount = balance * risk_per_trade
    size = risk_amount / (stop_loss_pips * pip_value)
    return round(size, 2)
