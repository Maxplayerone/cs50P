def main():
    adieufy()

def adieufy():
    responses = []
    while True:
        response = input("Name: ")

        if(response.lower() == "quit"):
            break

        responses.append(response)

    message = "Adieu, adieu, to "
    for index in range(len(responses)):
        if(index == len(responses) - 1 and len(responses) > 1):
            message  = message + " and " + responses[index]
        elif(index == 0):
            message = message + responses[index]
        else:
            message = message + ", " + responses[index]

    print(message)

if __name__ == "__main__":
    main()