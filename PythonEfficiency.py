import time

def brewCoffee():
    print("Start brewCoffee()")
    # Will take three seconds to complete
    time.sleep(3)
    print("End brewCoffee()")
    return "Brewing Complete"

def makeToast():
    print("Start makeToast()")
    # Two seconds to complete
    time.sleep(2)
    print("End makeToast()")
    return "Toasting complete"

# Record start times
def main():
    startTime = time.time()

    resultCoffee = brewCoffee()
    resultToast = makeToast()

    endTime = time.time()

    elapsedTime = endTime - startTime
    # Display results
    print(f"Brew result: {resultCoffee}")
    print(f"Toast result: {resultToast}")
    print(f"Total time elapsed: {elapsedTime:.2f} seconds")

if __name__ == "__main__":
    main()