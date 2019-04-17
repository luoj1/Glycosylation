#include <string>
#include <iostream>
#include <fstream>

class Csv_lib{
		ofstream csv;
	public:
		Csv_lib(string s){
			ofstream myfile;
			myfile.open("");
			myfile
		}
		int read_csv_line(vector<int> &out){

		}
		~Csv_lib(){
			csv.close();
		}

}