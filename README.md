<h1>Balance Python App</h1>


<h2>Description</h2>
    <p>
        This project demonstrates a simple bank account application implemented in Python. Users can view their account information, deposit money, and withdraw funds.
    </p>



<h2>Features</h2>
    <ul>
        <li>The Account class contains basic information like the account holder's name, account number, and balance.</li>
        <li>The <code>account_info()</code> method is used to display the account holder's details on the screen.</li>
        <li>The <code>deposit()</code> method allows users to deposit a specified amount of money into their account.</li>
        <li>The <code>withdraw()</code> method allows users to withdraw a specified amount of money from their account, provided they have sufficient balance.</li>
        <li>The <code>clear_term()</code> function is used to clear the terminal screen (works only on Windows).</li>
    </ul>



<h2>How to Use</h2>
    <p>
        1. Create an account using the <code>Account</code> class, providing the account holder's name, account number, and initial balance.
    </p>
    <pre><code>acc = Account("Berkay Kocak", 170777, 1000)</code></pre>
    <p>
        2. Start a loop to perform account operations:
    </p>
    <pre><code>while True:
    choice = int(input("What operation would you like to perform? (To view account information, enter 1, to deposit money, enter 2, to withdraw money, enter 3, to exit, enter 0):"))
  
</code></pre>


