def WER(referenceText, hypothesisText):
    brokenReferenceText = referenceText.split()
    brokenHypothesisText = hypothesisText.split()

    insertion = len(brokenHypothesisText) - len(brokenReferenceText)
    deletion = 0
    if (insertion < 0):
        deletion = abs(insertion)
        insertion = 0
    i = 0
    substitution = 0
    while(i < len(brokenHypothesisText) and i < len(brokenReferenceText)):
        if (brokenReferenceText[i] != brokenHypothesisText[i]):
            substitution += 1
        i += 1

    wer = ((insertion + deletion + substitution)/(len(brokenReferenceText)))*100
    return wer

def SubjectWERAvegrage():
    googleTests = "Google"
    IBMTests = "IBM"
    services = [googleTests, IBMTests]
    googleWER = 0
    IBMWER = 0
    countryGoogle = [0, 0, 0, 0, 0, 0]
    countryIBM = [0, 0, 0, 0, 0, 0]
    maleCountryGoogle = [0, 0, 0, 0, 0, 0]
    femaleCountryGoogle = [0, 0, 0, 0, 0, 0]
    maleCountryIBM = [0, 0, 0, 0, 0, 0]
    femaleCountryIBM = [0, 0, 0, 0, 0, 0]
    outputFile = open('output.txt', 'w+')
    for i in range(48):
        totalWER = 0
        inputFile = open(str(i+1) + '.txt', 'r')
        refText = ''
        hypoText = ''
        subject = inputFile.readline()
        country = inputFile.readline()
        gender = inputFile.readline()
        outputFile.write('\n' + subject+country+gender)
        for j in range(10):
            refText = inputFile.readline()
            hypoText = inputFile.readline()
            wer = WER(refText, hypoText)
            totalWER = totalWER + wer
            outputFile.write("Statement " + str(j) + " WER: " + str(wer) + "% or in Decimal " +  str(wer/100) + '\n')
        outputFile.write("Average WER :" + str(totalWER/10) + '\n')
        #Google Calcuations
        if i < 24:
            googleWER = googleWER + totalWER/10
            print(i//4)
            countryGoogle[i//4] = countryGoogle[i//4] + (totalWER/10)
            if (gender == "M\n"):
                maleCountryGoogle[i//4] = maleCountryGoogle[i//4] + (totalWER/10)
            if (gender == "F\n"):
                femaleCountryGoogle[i//4] = femaleCountryGoogle[i//4] + (totalWER/10)
            if (i%4 == 3):
                outputFile.write('\n')
                outputFile.write("Country Male WER for Google: " + str(maleCountryGoogle[i//4]/2) + '\n')
                outputFile.write("Country Female WER for Google: " + str(femaleCountryGoogle[i//4]/2) + '\n')
                outputFile.write("Country WER for Google " + country + ": " + str(countryGoogle[i//4] / 4) + '\n')
        #IBM calculations
        else:
            IBMWER = IBMWER + totalWER/10
            print(i//4 - 6)
            countryIBM[i//4 - 6] = countryIBM[i//4 - 6] + (totalWER/10)
            if (gender == "M\n"):
                maleCountryIBM[i//4 - 6] = maleCountryIBM[i//4 - 6] + (totalWER/10)
            if (gender == "F\n"):
                femaleCountryIBM[i//4 - 6] = femaleCountryIBM[i//4 - 6] + (totalWER/10)
            if (i%4 == 3):
                outputFile.write('\n')
                outputFile.write("Country Male WER for IBM: " + str(maleCountryIBM[i//4 - 6]/2) + '\n')
                outputFile.write("Country Female WER for IBM: " + str(femaleCountryIBM[i//4 - 6]/2) + '\n')
                outputFile.write("Country WER for IBM " + country + ": " + str(countryIBM[i//4 - 6] / 4) + '\n')
        #print(gender)
        inputFile.close()
    outputFile.write('\n')
    outputFile.write('Data Subset System and Gender\n')
    outputFile.write('Males in Google: ')
    outputFile.write(str(sum(maleCountryGoogle)/12) + '\n')
    outputFile.write('Females in Google: ')
    outputFile.write(str(sum(femaleCountryGoogle)/12) + '\n')
    outputFile.write('Males in IBM: ')
    outputFile.write(str(sum(maleCountryIBM)/12) + '\n')
    outputFile.write('Females in IBM: ')
    outputFile.write(str(sum(femaleCountryIBM)/12) + '\n')

    outputFile.write('\n')
    outputFile.write('Data Subset Gender\n')
    outputFile.write('Males: ')
    outputFile.write(str((sum(maleCountryGoogle) + sum(maleCountryIBM))/24) + '\n')
    outputFile.write('Female: ')
    outputFile.write(str((sum(femaleCountryGoogle) + sum(femaleCountryIBM))/24) + '\n')
    
    outputFile.write('\n')
    outputFile.write("Google's WER :" + str(googleWER/24) + '\n')
    outputFile.write("IBM's WER :" + str(IBMWER/24) + '\n')
    outputFile.close()
    
        

SubjectWERAvegrage()
