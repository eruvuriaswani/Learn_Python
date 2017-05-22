var IDMark_A = "_a";


function changeCheckbox(node, status) {
    var btn = $("#fsl_" + node.tId);
    if (btn.attr("checked") != status) {
        btn.attr("checked", Boolean(status));
    }
}

function isSelectNode(node) {
    return $("#fsl_" + node.tId).attr("checked");
}

function isSelectAllChildNoes(node) {
    var childNodes = node.children;
    if (childNodes) {
        for (var i = 0; i < childNodes.length; i++) {
            if (!isSelectNode(childNodes[i])) {
                return false;
            }
        }
    }
    return true;
}

function changeAllChildNoes(node, status) {
    var childNodes = node.children;
    if (childNodes) {
        for (var i = 0; i < childNodes.length; i++) {
            changeCheckbox(childNodes[i], status);
            changeAllChildNoes(childNodes[i], status);
        }
    }
}

function changeAllParentNoes(node, status) {
    var parentNode = node.getParentNode();
    if (parentNode) {
        if (status) {
            if (isSelectAllChildNoes(parentNode)) {
                changeCheckbox(parentNode, status);
            }
        } else {
            changeCheckbox(parentNode, status);
        }
        changeAllParentNoes(parentNode, status);
    }
}

function change(node, btn) {
    var status = btn.attr("checked");
    changeAllChildNoes(node, status);
    changeAllParentNoes(node, status);
}

function addDiyDom(treeId, node) {
    var aObj = $("#" + node.tId + IDMark_A);
    if (node.isParent) {
        aObj.before("<input type='checkbox' class='checkboxBtn' id='fsl_" + node.tId + "'></input>");
    } else {
        aObj.before("<input type='checkbox' class='checkboxBtn' id='fsl_" + node.tId + "' " +
            "value='" + node.id + "' name='case_list'></input>");
    }
    var btn = $("#fsl_" + node.tId);
    btn.bind("change", function () {
        change(node, btn);
    })
}

function openUpperPath(treeObj, node) {
    var parentNode = node.getParentNode();
    if (parentNode) {
        //if (parentNode.open) {
            treeObj.expandNode(node, true);
        //}
        openUpperPath(treeObj, parentNode)
    }
}

function echoNode(treeObj, node, isOpenPath) {
    if (isOpenPath == null || isOpenPath) {
        openUpperPath(treeObj, node);
    }
    changeCheckbox(node, true);
    changeAllChildNoes(node, true);
    changeAllParentNoes(node, true);
}