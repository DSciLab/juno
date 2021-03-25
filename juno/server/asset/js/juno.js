'use strict';
class ElementManager {
    constructor() {
        this.classMap = new Map();
        this.idMap = new Map();
    }

    getElementById(idName) {
        if (this.idMap.get(idName) == undefined) {
            // get element from DOM
            let ele = document.getElementById(idName);
            if (ele == null) {
                throw new Error("Element undefine" + "(" + idName + ")");
            } else {
                // save element to idMap
                this.idMap.set(idName, ele);
            }
        }

        // get element from map
        return this.idMap.get(idName);
    }

    getElementByClassName(className) {
        if (this.classMap.get(className) == undefined) {
            // get element from DOM
            let ele = document.getElementByClassName(className);
            if (ele == null) {
                throw new Error("Element undefine" + "(" + className + ")");
            } else {
                // save element to classMap
                this.classMap.set(className, ele);
            }
        }

        // get element from map
        return this.classMap.get(className);
    }

    registeEventByClassName(className, fn) {

    }

    registeEventById(isName, fn) {

    }
}


class WSManager {
    constructor(addr) {
        this.socket = new WebSocket(addr);
        this.socket.addEventListener('open', function (event) {
            console.log('WS connected.');
        });
        this.socket.addEventListener('close', function (event) {
            console.log('WS colsed.');
        });
        this.socket.addEventListener('error', function (event) {
            console.log('WS error.');
        });
        this.socket.addEventListener('message', function (event) {
            console.log('WS revice message.');
        });
    }

    sentMSG(msg) {
        this.socket.send(msg);
    }

    onMSG(fn) {

    }
}
