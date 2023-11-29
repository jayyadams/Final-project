import React from "react";

function Checkout({items, }) {
    return (
    <div align='center'>
        <img src="/images/cart.gif" />
        <h2>Cart...?</h2>
        <p>{items}</p>
    </div>
)}

export default Checkout