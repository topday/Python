# Python - Raspberry Pi 

## Send SMS using GSM modem SIM800/SIM900

`send_sms.py` - quick list of commands require to send SMS using SIM800 micro modem.

SendSMS object is ready to use and should work straight away. Instatiated object will make hanshake and will ensure that modem is set into "correct" state.

### Send single SMS sample
```
sms =  SendSMS()
sms.sendText('<your phone number>', 'my text message') 
```

### Other useful commands
```
sms =  SendSMS()
sms.receiveSMS()
sms.deleteSMS()
sms.getIMEI()
```
