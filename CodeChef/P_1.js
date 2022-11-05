/*Problem 1-  (From codechef)
Chef took an examination two times. 
In the first attempt, he scored XX marks while in the second attempt he scored YY marks. 
According to the rules of the examination, the best score out of the two attempts will be considered as the final score.*/

console.log("\n\n\n                Problem number 1\n");

const readline = require("readline");

const input1 = readline.createInterface(
    {input: process.stdin, 
    output: process.stdout,}); //function with 2 arguments (input, output)

input1.question("Scores of first attempt - ",
    (answer1) => {
        input1.question("Scores of second attempt - ", 
        (answer2)=> {
            if (+answer1 > +answer2)
                console.log(`Best score of them both is - ${answer1}`)
            else
                console.log(`Best score of them both is - ${answer2}`)
            
            console.log('\n\n\n')
            input1.close()
        })
    }
);