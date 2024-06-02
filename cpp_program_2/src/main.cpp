#include "DataProcessor.h"

int main() {
    setlocale(LC_ALL, "Russian");
    DataProcessor processor;
    if (processor.processFile("../../../python_program_1/data.csv")) {
        processor.writeOutput("output.csv");
    }

    return 0;
}
