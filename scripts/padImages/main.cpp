#include <iostream>
#include <vector>
#include <dirent.h>
#include <unistd.h>
#include <thread>
#include <sstream>
#define THREADS_NB 4
using namespace std;

template<typename T>
string convertNbToStr(const T& number)
{
    ostringstream convert;
    convert << number;
    return convert.str();
}

char pathSeparator = '/';
vector<string> listFiles(string directory);
void print(string s);
unsigned int toDo;
string exec(string cmd),
       escapeShellArgument(string shellArgument),
       replaceAll(string str, const string& from, const string& to);

vector<string> files;
string commonFolder = "formula_images_processed",
       sourceFolder = commonFolder + "/",
       destinationFolder = commonFolder + "_padded/";

void work(unsigned int beginIndex, unsigned int endIndex)
{
	for(unsigned int index = beginIndex; index < endIndex; index++)
	{
		string file = files[index],
		       command = "convert " + escapeShellArgument(sourceFolder + file) + " -gravity NorthWest -background white -extent 680x173 " + escapeShellArgument(destinationFolder + file);
		exec(command);
		toDo--;
	}
}

int main()
{
	string workingFolder = "/mnt/c/Users/Benjamin/Desktop/BensFolder/School/ENS/Saclay/M1/DeepLearning/Project/im2latex/processed/";
	
	chdir(workingFolder.c_str());

	files = listFiles(sourceFolder);

	unsigned int filesSize = files.size(),
				 slice = filesSize / THREADS_NB;
	toDo = filesSize;
	thread threads[THREADS_NB];
	for(unsigned short threadsIndex = 0; threadsIndex < THREADS_NB; threadsIndex++)
		threads[threadsIndex] = thread(work, threadsIndex * slice, threadsIndex == THREADS_NB - 1 ? filesSize : (threadsIndex + 1) * slice);
	//for(unsigned short threadsIndex = 0; threadsIndex < THREADS_NB; threadsIndex++)
	//	threads[threadsIndex].join();
	while(toDo > 0)
	{
		sleep(1);
		print(convertNbToStr(filesSize - toDo) + " / " + convertNbToStr(filesSize));
	}
	
	return 0;
}

bool startsWith(string subject, string test)
{
    return !subject.compare(0, test.size(), test);
}

string replace(string subject, const string& search, const string& replace = "")
{
    unsigned int s = subject.find(search);
    if(s > subject.length())
        return subject;
    return subject.replace(s, search.length(), replace);
}

void listFiles(string direc, vector<string>* str)
{
    DIR* dir;
    struct dirent* ent;
    if((dir = opendir(direc.c_str())) != NULL)
    {
        while((ent = readdir(dir)) != NULL)
        {
            string file = ent->d_name;
            if(!startsWith(file, "."))
            {
                string path = direc;
                if(path[path.length() - 1] != pathSeparator)
                    path += pathSeparator;
                path += file;
                if(file.find_last_of(".") > file.length())
                    listFiles(path, str);
                else
                    str->push_back(path);
            }
        }
        closedir(dir);
    }
}

vector<string> listFiles(string directory)
{
    vector<string> files;
    listFiles(directory, &files);
	unsigned int filesSize = files.size();
	for(unsigned int filesIndex = 0; filesIndex < filesSize; filesIndex++)
		files[filesIndex] = replace(files[filesIndex], directory);
    return files;
}

string exec(string cmd)
{
    array<char, 128> buffer;
    string result;
    unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd.c_str(), "r"), pclose);
    if(!pipe)
        throw runtime_error("popen() failed!");
    while(fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr)
        result += buffer.data();
    return result;
}

void print(string s)
{
	cout << s << endl;
}

string replaceAll(string str, const string& from, const string& to)
{
    size_t start_pos = 0;
    while((start_pos = str.find(from, start_pos)) != string::npos)
    {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length(); // Handles case where 'to' is a substring of 'from'
    }
    return str;
}

// Source: https://stackoverflow.com/a/3669819
string escapeShellArgument(string shellArgument)
{
    return "'" + replaceAll(shellArgument, "'", "'\\''") + "'";
}
