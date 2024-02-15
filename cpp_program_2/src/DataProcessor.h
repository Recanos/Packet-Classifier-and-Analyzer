#ifndef DATAPROCESSOR_H
#define DATAPROCESSOR_H

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>

class DataProcessor {
private:
    std::map<std::string, std::vector<int>> dataMap;

public:
    bool processFile(const std::string& filename);
    bool writeOutput(const std::string& filename);
};

#endif // DATAPROCESSOR_H
