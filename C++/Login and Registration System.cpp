#include <iostream> // using input and output
#include <fstream>  // file stream
#include <string>


using namespace std;

bool IsLoggedIn(){
  string username, password, un, pw;

  cout<<"Enter Username: ";
  cin >> username;
  cout<<"Enter Password: ";
  cin>> password;

  ifstream read(username + ".txt");

  getline(read, un);
  getline(read, pw);

  if (un == username && pw == password){
    return true;
  }
  else{
    return false;
  }
}

int main() {
  int choice;

  cout<<"1. Register\n2.Login\nYour choice: ";
  cin >> choice;

  if(choice == 1){
    string username, password;

    cout<< "Select a username: "; cin>>username;
    cout<< "Select a password: "; cin>>password;
    
    ofstream file;
    file.open(username + ".txt");
    file << username << endl << password;
    file.close();

    main();
  }
  else if(choice == 2){
    bool status = IsLoggedIn();

    if(!status){
      cout << "False Login!"<<endl;
      return 1;
    }
    else{
      cout<<"Welcome to the Club!"<<endl;
      return 0;
    }
  }
}
