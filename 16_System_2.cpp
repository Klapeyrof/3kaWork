#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

unsigned long long int get_a_hexadecimal() {
    char c;
    int k = 0,i=0,len,LEN,symv;
    unsigned long long int Summ=0;
    vector <char> lst;

    string str;
    getline(cin, str);
    LEN=str.length();
    len = LEN;



    //Находим цифры и A,B,C,D,E,F в строке
    do {
        c = str[i];
        if (('A' <= c and c <= 'F') or ('0' <= c and c <= '9') or ('a' <= c and c <= 'f')) {
            k++;
            lst.push_back(c);
        }
        i++;
        len--;
    } while (len>0);


    if (lst[0] == '0') {
        return 0;
    }




    int step = k-1;
    for (i = 0; i < k; i++) {
        //Преобразуем символ в число от 0 до 15
        if ('0' <= lst[i] and lst[i] <= '9') {
            symv = int(lst[i]) - 48;
        }
        if ('A' <= lst[i] and lst[i] <= 'F') {
            symv = int(lst[i]) - 55;
        }
        if ('a' <= lst[i] and lst[i] <= 'f') {
            symv = int(lst[i]) - 87;
        }
        //Получаем число 16-ричной системе
        Summ += symv * pow(16, step);
        step--;
    }

    return Summ;
}


// ваша реализация функции
int main()
{
    cout << get_a_hexadecimal() << endl;
    return 0;
}
