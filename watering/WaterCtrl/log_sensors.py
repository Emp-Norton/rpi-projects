import utils as u
import setup as s
import vars as v

inputs = s.run_setup()

readings = u.read_all_pins(inputs, write_logs=True)

# Todo fix crontab running the testing script -- needs an operator to indicate when to quit



