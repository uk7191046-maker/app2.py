const express=require("express");
const app=express();
app.use(express.json());
function logger(req,res,next){
    console.log("method:",req.method);
    console.log("url:",req.url);
    next();
}
app.use(logger);
let products=[
    {id:1,name:"laptop",price:5000},
    {id:2,name:"mouse",price:500}
]
app.get("/products", (req, res) => {
    res.status(200).json({
        success: true,
        message: "products retrieved successfully",
        data:products
     });
});

app.post("/products", (req, res) => {
    const { name, price } = req.body;

    if (!name) {
        return res.status(400).json({
            success: false,
            message: "product name is required"
        });
    }

    if (price <= 0) {
        return res.status(400).json({
            success: false,
            message: "product price must be greater than 0"
        });
    }

    const newProduct = {
        id: products.length + 1,
        name: name,
        price: price
    };
    products.push(newProduct);

    return res.status(201).json({
        success: true,
        message: "product created successfully",
        data: newProduct
    });
});
app.listen(3000,() => {
    console.log("Server is running on port 3000");
});
