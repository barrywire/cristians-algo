# Cristian's Algorithm

An implementation of Cristian's Algorithm in Ruby and Python.

## Algorithm

1. The process on the client side **sends** a request for fetching the time at the server at T0.
2. The clock server **listens** to the request made by the client process and returns the response in form of clock server time.
3. The client process **receives** the response from the server and calculates the time difference between the client and the server using the formula:

   ```
   Tclient = T0 + (T1 - T0)/2
   ```
