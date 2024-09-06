/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    var ransom=ransomNote.split('');
    var mag=magazine.split('');
    var lists=[];
    var canMake=true;
    for(var i=0;i<ransom.length;i++){
        for(var j=0;j<mag.length;j++){
            if(ransom[i]==mag[j]){
                lists.push(`${mag[j]}`);
                mag.splice(j,1);
                
                break;
            }
        }
    }
    return JSON.stringify(lists) === JSON.stringify(ransom);
};