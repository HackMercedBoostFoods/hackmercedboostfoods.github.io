

const { MongoClient, ServerApiVersion } = require('mongodb');
const uri = "mongodb+srv://cboiteux:bxXhBVy5wS5qb5Pn@cluster0.4vyuo5v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

async function run() {
  try {
    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();
    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log("Pinged your deployment. You successfully connected to MongoDB!");
    const dbName = "CropDB";
    const collectionName = "users";
    const database = client.db(dbName);
    const collection = database.collection(collectionName);
    const newUsers = [
        {
          username: "testttt",
          password: "jfdsakfd",
        },
        
        {
            username: "jfdska3",
            password: "342ufds0",
        },
      ];
    
      try {
        const insertManyResult = await collection.insertMany(newUsers);
        console.log(`${insertManyResult.insertedCount} documents successfully inserted.\n`);
      } catch (err) {
        console.error(`Something went wrong trying to insert the new documents: ${err}\n`);
      }
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);





// /* global use, db */
// // MongoDB Playground
// // To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// // Make sure you are connected to enable completions and to be able to run a playground.
// // Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// // The result of the last command run in a playground is shown on the results panel.
// // By default the first 20 documents will be returned with a cursor.
// // Use 'console.log()' to print to the debug output.
// // For more documentation on playgrounds please refer to
// // https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// const uri = "";
// // Select the database to use.

// // Run a find command to view items sold on April 4th, 2014.
// // const salesOnApril4th = db.getCollection('sales').find({
// //   date: { $gte: new Date('2014-04-04'), $lt: new Date('2014-04-05') }
// // }).count();

// // // Print a message to the output window.
// // console.log(`${salesOnApril4th} sales occurred in 2014.`);

// // // Here we run an aggregation and open a cursor to the results.
// // // Use '.toArray()' to exhaust the cursor to return the whole result set.
// // // You can use '.hasNext()/.next()' to iterate through the cursor page by page.
// // db.getCollection('sales').aggregate([
// //   // Find all of the sales that occurred in 2014.
// //   { $match: { date: { $gte: new Date('2014-01-01'), $lt: new Date('2015-01-01') } } },
// //   // Group the total sales for each product.
// //   { $group: { _id: '$item', totalSaleAmount: { $sum: { $multiply: [ '$price', '$quantity' ] } } } }
// // ]);
