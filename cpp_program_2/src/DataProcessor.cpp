#include "DataProcessor.h"

bool DataProcessor::processFile(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Не удалось открыть файл для чтения: " << filename << std::endl;
        return false;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::vector<std::string> data;
        std::map<std::string, std::vector<int>>::iterator it;

        std::stringstream lineStream(line);
        std::string cell;

        while (std::getline(lineStream, cell, ',')) {
            data.push_back(cell);
        }

        it = dataMap.find(data[0]);
        if (it == dataMap.end()) {
            dataMap[data[0]] = { 0, 0, std::stoi(data[4]), std::stoi(data[5]) };
        }
        else {
            dataMap[it->first][2] += std::stoi(data[4]);
            dataMap[it->first][3] += std::stoi(data[5]);
        }

        it = dataMap.find(data[1]);
        if (it == dataMap.end()) {
            dataMap[data[1]] = { std::stoi(data[4]), std::stoi(data[5]), 0, 0 };
        }
        else {
            dataMap[it->first][0] += std::stoi(data[4]);
            dataMap[it->first][1] += std::stoi(data[5]);
        }
    }

    file.close();
    return true;
}

bool DataProcessor::writeOutput(const std::string& filename) {
    std::ofstream output_file(filename);
    if (!output_file.is_open()) {
        std::cerr << "Не удалось открыть файл для записи: " << filename << std::endl;
        return false;
    }

    for (auto it = dataMap.begin(); it != dataMap.end(); ++it) {
        output_file << it->first << ","
            << it->second[0] << ","
            << it->second[1] << ","
            << it->second[2] << ","
            << it->second[3] << std::endl;
    }

    output_file.close();
    std::cout << "Данные успешно записаны в файл " << filename << std::endl;
    return true;
}
