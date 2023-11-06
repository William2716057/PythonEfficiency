import time

def brewCoffee():
    print("Start brewCoffee()")
    #will take three seconds to complete
    time.sleep(3)
    print("End brewCoffee()")
    return "Brewing Complete"

def makeToast():
    print("Start toast()")
    #two seconds to complete
    time.sleep(2)
    print("End toasting()")
    return "Toasting complete()"

#record start times
def main():
    startTime = time.time()

    resultCoffee = brewCoffee()
    resultToast = makeToast()

    endTime = time.time()

    elapsedTime = endTime - startTime
