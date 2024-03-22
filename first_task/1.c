#include <stdio.h>
#include <math.h>


int find_double() {
    double e = 1.0;
    int counter = 0;

    while (1 + e != 1) {
        counter++;
        e /= 2;
    }

    return counter - 1;
}


double find_half_e() {
    double e = 1.0;
    int counter = 0;

    while (1 + e != 1) {
        counter++;
        e /= 2;
    }

    return e;
}


int find_float() {
    float e = 1.0;
    int counter = 0;

    while (1 + e != 1) {
        counter++;
        e /= 2;
    }

    return counter - 1;
}


int find_power_double() {
    double e = 1.0;
    int counter = 0;

    while (!isinf(e)) {
        counter++;
        e *= 2;
    }

    return counter;
}


int find_power_float() {
    float e = 1.0;
    int counter = 0;

    while (!isinf(e)) {
        counter++;
        e *= 2;
    }

    return counter;
}


void compare() {
    double half_e = find_half_e();
    double e = half_e * 2;

    if (1.0 == 1.0 + half_e) {
        printf("1 is equal to 1 + e/2\n");
    }
    if (1 + half_e < 1 + e){
        printf("1 + e/2 less then 1 + e\n");
    }
    if (1 + e + half_e > 1 + e){
        printf(" %f, %f, %f \n", 1 + e + half_e, 1 + e, half_e);
        printf("1 + e + e/2 is greater then 1 + e\n");
    }
}


int find_min(){
    double e = 1.0;
    int counter = 0;

    while (e != 0) {
        counter++;
        e /= 2;
    }

    return counter;
}


int main() {
    printf("%d ", find_min());
    printf("%d  \n", find_double());
    printf("%d \n", find_power_double());
    compare();
    return 0;
}