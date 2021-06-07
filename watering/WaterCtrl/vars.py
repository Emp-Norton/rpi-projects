''' Default values for pupms in prototype. There's a much better way but it's low priority '''

# TODO: If drip irrigation not effective, not implementable in the remaining time, or not measurable, make this support 1:1 pump:watering_group
PUMP_CTRL_PIN = 14

PUMP_PINS = [14, 15, 18] 
# Pump Layout IIRC:
## 14 is first pump, going to Tradescantia Zebrinas and Small Succulents, 
## 15 is middle pump, presumably larger succulents and a pothos?
## 18 is 12V pump powered by wall plug, going to herbs, prayer plant,pothos? 

# TODO: create defaults for watering groups? This magic number won't last beyond testing
NUM_INPUTS = 5
# TODO: Upate this after testing
DEFAULT_PUMP_SECONDS = 30

