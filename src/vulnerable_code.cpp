#include <iostream>

void processTransaction() {
    char accountBuffer[10]; // Fixed-size storage array
    std::cout << "Enter Gateway Account ID: ";
    
    // CRITICAL FLAW: Unchecked streaming into a fixed memory container.
    // Entering more than 9 characters triggers a Stack Buffer Overflow.
    std::cin >> accountBuffer; 
    
    std::cout << "Transaction registered for Account: " << accountBuffer << std::endl;
}

int main() {
    processTransaction();
    return 0;
}