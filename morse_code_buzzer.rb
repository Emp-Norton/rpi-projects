# TODO : Decoder, buzzer-pin abstraction, continual read-react
require 'rpi_gpio'

RPi::GPIO.set_warnings(false)
RPi::GPIO.set_numbering :bcm 
RPi::GPIO.setup 15, :as => :output, :initialize => :low # number of pin to use as buzzer (broadcom numbering) 

#RPi::GPIO.setup 2, :as => :output, :initialize => :low # these are commented out for simplicity. They represent blue and red leds..
#RPi::GPIO.setup 18, :as => :output, :initialize => :low #..which I used at night in leiu of a loud buzzer. An array of pins can be passed to #activate, facilitating this use case. 

@morse = {}

@morse['a'] = '. -'
@morse['b'] = '- . . .'
@morse['c'] = '- . - .'
@morse['d'] = '- . .'
@morse['e'] = '.' 
@morse['f'] = '. . - .'
@morse['g'] = '- - .'
@morse['h'] = '. . . .' 
@morse['i'] = '. .'
@morse['j'] = '. - - -'
@morse['k'] = '- . -'
@morse['l'] = '. - . .'
@morse['m'] = '- -'
@morse['n'] = '- .' 
@morse['o'] = '- - -' 
@morse['p'] = '. - - .'
@morse['q'] = '- - . -'
@morse['r'] = '. - .' 
@morse['s'] = '. . .' 
@morse['t'] = '-' 
@morse['u'] = '. . -' 
@morse['v'] = '. . . -' 
@morse['w'] = '. - -' 
@morse['x'] = '- . . =' 
@morse['y'] = '- . - -' 
@morse['z'] = '- - . .' 

def activate(pins) #just a timesaver to avoid typing RPi::GPIO...etc. Accepts array of pins to activate
  pins.each{ | pin |  RPi::GPIO.set_high pin }
end

def deactivate(pins)
  pins.each{ | pin |  RPi::GPIO.set_low pin }
end 

def buzz(duration) 
  case duration
   when "dit"
      activate([15]) # the pin connected to the buzzer. working on abstracting this
      sleep(0.1)
      deactivate([15]) # DRY. This needs to be cleaned up. Maybe a proc?
   when "dah" 
      activate([15])
      sleep(0.3)
      deactivate([15])
   when "break"
      sleep(0.7)
      deactivate([15])
    end 
end 


def morse_encoder(str)
  coded = []
  words = str.split(" ")
  words.each do | word | 
    letters=word.split("") 
    letters.each do | letter | # map might be a little cleaner
      coded.push(@morse[letter])
    end 
  coded.push(" ")
  end  
return coded.join(" ")
end 

def transmit(encoded_message)
words = encoded_message.split("  ")
words.each do | word |
  chars = word.split("")
  chars.each do | char |
    case char 
      when "-" 
        buzz("dah")
      when  "."
        buzz("dit")
      else sleep(0.3) #pause between letters
      end 
    end 
    buzz("break") #pause between words
  end 
puts "Transmission sent"
clean([15])
end

def clean(pins) 
pins.each{ | pin | RPi::GPIO.set_low pin } 
end

print "Please enter message to transmit: " 
message = gets.chomp 
encoded_message = morse_encoder(message) 
transmit(encoded_message)

