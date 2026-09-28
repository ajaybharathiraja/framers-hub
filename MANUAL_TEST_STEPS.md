# Manual Verification Steps

Here are the exact manual click-through steps to verify the two-step pricing flow natively in your browser:

1. **Login**: Go to the login page and log in as a farmer.
2. **Profile Check**: Navigate to your farmer dashboard/profile. Ensure that your **State** is `Tamil Nadu` and your **District** is `Ariyalur` (this is necessary to map to our real backend CSV dataset).
3. **Start Flow**: Go to the **My Products** page and click **Add New Product** (`/farmer/products/add/`).
4. **Draft Submission**: 
   - Enter `Tomato` for the **Commodity** field.
   - Enter `Ariyalur(Uzhavar Sandhai)` exactly for the **Location** field (this maps exactly to the real market in the dataset).
   - Fill out the rest of the fields (like `Total Quantity`).
   - Click the **Add Product** button.
5. **Observe Pricing Prediction**: 
   - You will automatically be redirected to `/farmer/products/<id>/pricing/`.
   - On page load, wait a second; the JavaScript will execute the fetch call using your listing ID, query the AI, and display the predicted price directly on the screen!
6. **Set Final Price**:
   - In the same page, enter `45.00` in the **Selling Price Per Kg** box at the bottom.
   - Click **Publish Listing**.
7. **Database Verification**:
   - The UI will redirect you back to the My Products page, showing your listing is now active.
   - Open your django shell `python manage.py shell`, import the `Listing` model, and retrieve this listing. You will see both `ai_predicted_price` and `reference_market_price` perfectly populated alongside your actual set `selling_price_per_kg`.
   - You can also check `ResearchEvent.objects.last().metadata` to see the event recorded your final price alongside the AI's predicted price.
