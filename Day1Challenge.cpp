#include <iostream>
#include <fstream>
#include <string>
#include <regex>
using namespace std;

string replaceSpelledNumbers(string input) { // Replaces any given numbers in text into digits
    string numbers[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    string replaceValues[] {"on1e", "tw2o", "thr3ee", "fo4ur", "fi5ve", "si6x", "sev7en", "eig8ht", "ni9ne"}; // Alas I cannot take credit for this ingenious solution to edge cases, thank you random reddit user

    string returnString = input;
    int counter = 0;
    for (string &number : numbers) {
        returnString = std::regex_replace(returnString, std::regex(number), replaceValues[counter]);
        counter++;
    }
    return returnString;
}

int main() {
    // Import the file
    ifstream contentFile("Day1Content.txt");

    string inputText;
    string numbersText;

    int sum = 0;
    int strangeNumber = 0;

    while (getline(contentFile, inputText)) {
        int firstNumber = -1;
        int lastNumber = -1;

        // Replace the words with digits
        string input = replaceSpelledNumbers(inputText);

        for (int iter = 0; iter < input.size(); iter++) {
            if (isdigit(input[iter])) {
                if (firstNumber == -1) {
                    firstNumber = int(input[iter]) - 48; // Because it converts it to ascii, 47 is the character before 0
                } else {
                    lastNumber = int(input[iter]) - 48;
                }
            }
        }
        int numberToAdd = 0;
        if (firstNumber != -1 and lastNumber != -1) {
            numberToAdd = firstNumber * 10 + lastNumber;
        } else if (firstNumber != -1) { // lastNumber must be the uninitialized one
            numberToAdd = firstNumber * 11; // Because 10 for the tens place and one for the ones place
        }
        sum += numberToAdd;
        strangeNumber = numberToAdd;
    }
    contentFile.close();
    cout << '\n' << sum << "\n";
}