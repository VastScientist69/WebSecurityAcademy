Race Condition Lab Solution
Overview
This lab demonstrates a race condition vulnerability in a single endpoint that handles coupon applications during checkout.

Tools Needed
Web browser with Burp Suite (or similar proxy tool)

Turbo Intruder (Burp Suite extension)

Steps to Solve
Add item to cart and proceed to checkout.

Intercept the request when applying a discount coupon.

Identify the vulnerable endpoint - typically a POST request to /cart/coupon with parameters like csrf and coupon.

Send the request to Turbo Intruder for simultaneous attacks.

Use this Turbo Intruder script:

python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=20,
                           requestsPerConnection=20,
                           pipeline=False)
    
    for i in range(20):
        engine.queue(target.req, i)
        
    for i in range(20):
        engine.queue(target.req, i)

def handleResponse(req, interesting):
    table.add(req)
Configure the attack:

Use the intercepted coupon application request

Set high concurrent connections (20-30)

Execute the attack

Observe the results - multiple successful coupon applications should stack, giving excessive discount.

Complete the purchase with the heavily discounted price.

Key Points
The vulnerability allows multiple coupon applications to process before the system can validate usage limits

Race conditions exploit the tiny time gap between validation and execution

No authentication bypass needed - this is purely about timing exploitation

The lab should be solved once you successfully exploit the race condition to apply the coupon multiple times and complete the purchase.

