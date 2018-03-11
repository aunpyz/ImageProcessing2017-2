#include<iostream>
#include<fstream>
#include<sstream>

int main(){
    using namespace std;
    ifstream file("scaled_shapes.pgm");
    ofstream outfile("out.txt");
    stringstream ss;
    string line;

    //x for column, y for row
    int x,y;

    //get first line
    getline(file, line);
    //comment
    while(getline(file, line)){
        if(line[0] != '#'){
            stringstream ss;
            ss << line;
            //get # columns and rows
            ss >> x >> y;
            break;
        }
    }

    //ss << file.rdbuf();

    //get rid of gray level identifier
    //ss >> line;

    //experiment
    /*
    line = "abcde\nfghij\nklmno";
    ss.str(string());
    ss << line;
    unsigned char c;
    for(int i=0; i<3; ++i){
        for(int j=0; j<5; ++j){
            ss>>c;
            outfile<<c<<" ";
            if(ss.eof()){
                cout<<"end\n";
                break;
            }
        }
        outfile<<endl;
    }
    cout<<ss.str();
    */

    //pixel value
    /*
    unsigned char ch[x][y];
    for(int i=0; i<y; ++i){
        for(int j=1; j<x; ++j){

            if(ss.eof()){
                cout<<"end\n";
				goto endloop;
            }

            ss >> ch[j][i];
            outfile << ch[j][i];
        }
        outfile << endl;
    }*/

    for(int i=0; i<y; ++i){
        for(int j=1; j<x; ++j){
            unsigned char c;
            file >> c;
            outfile << c;
        }
        outfile << endl;
    }
	endloop:
    return 0;
}
