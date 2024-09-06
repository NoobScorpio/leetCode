/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    var lists=[];
   for(var i=1;i<=n;i++){
        if(i%3==0 && i%5==0){
            lists.push("FizzBuzz");
        }
        else if(i%3==0){
            lists.push("Fizz");
        }
        else if(i%5==0){
            lists.push("Buzz");
        }
        else{
            lists.push(`${i}`);
        }
   }
    return lists;
};