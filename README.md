# <u>elec_toolkit</u>
Library, that provides different classes for calculating with physical values.
It is specially designed for tuition of signal-theory in electrical engineering.
Each class-instance represents a physical value, that can be combined with others.
The classes support basic mathematical operations on each other and always contain a unit and a description. 

## classes:
   *    ```Phys_unit```:<br/>real-valued, supports basic mathematical operations, callable (returns value (int or float) of itself), printable (returns formatted string with description, value and unit)
   *    ```Complex_phys_unit```:<br/>complex-valued, subclass of Phys_unit-class, supports basic mathematical operations, printable (returns formatted string with description, formatted complex value as complex representation and as amount-phase-representation with units).<br/>Instances are callable with positional argument to return value of the delayed sine for a specific time<br/><br/>Instances can be constructed from complex value (real, imaginary) or from amount-phase-representation (magnitude/phase of the resulting sine). <br/> The class provides classmethods to convert between complex- or amount-phase-representation (```complex_to_polar``` / ```polar_to_complex```).<br/><br/>Plot the complex vector-diagram with the ```plot``` method.