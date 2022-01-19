function LinkedList() {
    this.head = null;
    this.n_steps = 0; //The number of steps that the last operation took
    this.length = 0;

    /**
     * @param{object} val: An object to add to the list
     */
    this.insert = function(val) {
        this.n_steps = 1;
        if (this.head === null) {
            this.head = {'val':val, 'next':null};
            this.length = 1;
        }
        else {
            var ptr = this.head;
            if (ptr.val == val) {
                return;
            }
            while (!(ptr.next === null)) {
                this.n_steps += 1;
                ptr = ptr.next;
                if (ptr.val == val) {
                    return;
                }
            }
            this.n_steps += 1;
            //Add to end of list if not found
            ptr.next = {'val':val, 'next':null};
            this.length += 1;
        }
    }

    /**
     * @param{object} val: An object to remove from the list
     * @returns{object} The object removed from the list, or null if it wasn't there
     */
    this.delete = function(val) {
        this.n_steps = 1;
        var ptr = this.head;
        var prevptr = null;
        while (!(ptr === null)) {
            if (ptr.val == val) {
                if (prevptr === null) {
                    this.head = ptr.next;
                }
                else {
                    prevptr.next = ptr.next;
                }
                this.length -= 1;
                return ptr.val;
            }
            prevptr = ptr;
            ptr = ptr.next;
            this.n_steps += 1;
        }
        return null;
    }

    this.remove = this.delete;

    /**
     * @param{object} val: An object to search for in the list
     * @returns{boolean} true if in the list, false if not
     */
    this.contains = function(val) {
        this.n_steps = 1;
        var ptr = this.head;
        while (!(ptr === null)) {
            if (ptr.val == val) {
                return true;
            }
            ptr = ptr.next;
            this.n_steps += 1;
        }
        return false;
    }
}

function testLinkedList() {
    NTrials = 10000;
    MaxNum = 1000;
    mylist = new LinkedList();
    gtlist = {};

    for (var i = 0; i < NTrials; i++) {
        var num = Math.floor(Math.random()*MaxNum);
        mylist.insert(num);
        gtlist[num] = null;
        var addremove = Math.floor(Math.random()*2);
        if (addremove == 0) {
            //console.log("Delete " + num);
            delete gtlist[num];
            mylist.remove(num);
        }
        else {
            //console.log("Add " + num);
            gtlist[num] = num;
            mylist.insert(num);
        }
        //Now check all numbers
        for (var k = 0; k < MaxNum; k++) {
            var myres = mylist.contains(k);
            var gtres = k in gtlist;
            if (!(myres == gtres)) {
                console.log("ERROR: " + k + " in mylist = " + myres + ", " + k + " in gtlist = " + gtres);
            }
        }
    }
    console.log("mylist length = " + mylist.length);
    console.log("gtlist.length = " + Object.keys(gtlist).length);
}