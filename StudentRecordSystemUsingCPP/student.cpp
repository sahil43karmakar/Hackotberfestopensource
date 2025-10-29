#include <iostream>
#include <fstream>
using namespace std;

class Student {
public:
    int roll;
    string name;
    float marks;

    void input() {
        cout << "Enter Roll No: ";
        cin >> roll;
        cout << "Enter Name: ";
        cin.ignore();
        getline(cin, name);
        cout << "Enter Marks: ";
        cin >> marks;
    }

    void display() {
        cout << "Roll: " << roll << ", Name: " << name << ", Marks: " << marks << endl;
    }
};

void addStudent() {
    Student s;
    s.input();
    ofstream out("students.txt", ios::app);
    out << s.roll << " " << s.name << " " << s.marks << endl;
    out.close();
    cout << "✅ Student added successfully!\n";
}

void viewStudents() {
    Student s;
    ifstream in("students.txt");
    while (in >> s.roll >> s.name >> s.marks) {
        s.display();
    }
    in.close();
}

int main() {
    int choice;
    do {
        cout << "\n Student Record System\n";
        cout << "1. Add Student\n";
        cout << "2. View All Students\n";
        cout << "3. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1: addStudent(); break;
            case 2: viewStudents(); break;
            case 3: cout << " Exiting...\n"; break;
            default: cout << " Invalid choice!\n";
        }
    } while (choice != 3);

    return 0;
}