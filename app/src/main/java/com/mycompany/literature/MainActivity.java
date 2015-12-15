package com.mycompany.literature;

import android.app.*;
import android.os.*;
import android.view.*;
import android.widget.*;
import android.widget.AdapterView.*;

public class MainActivity extends Activity implements OnItemSelectedListener
{



	TextView playerData;
	
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
		

	playerData = (TextView)findViewById(R.id.playerData);
	displayPlayerCards();	
	

	Spinner asked_by_spin = (Spinner) findViewById(R.id.asked_by);
	Spinner resp_by_spin = (Spinner) findViewById(R.id.resp_by);
	Spinner asked_for_spin = (Spinner) findViewById(R.id.asked_for);
	
//	asked_by_spin.setOnItemSelectedListener(this);
//	resp_by_spin.setOnItemSelectedListener(this);
//	asked_for_spin.setOnItemSelectedListener(this);
//		
	// Create an ArrayAdapter using the string array and a default spinner layout
	ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,																		 R.array.planets_array, android.R.layout.simple_spinner_item);
	// Specify the layout to use when the list of choices appears
	adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
	
	// Apply the adapter to the spinner
	asked_by_spin.setAdapter(adapter);
    resp_by_spin.setAdapter(adapter);
	asked_for_spin.setAdapter(adapter);
	
	//Link spinner to listener
	asked_by_spin.setOnItemSelectedListener(this);
	resp_by_spin.setOnItemSelectedListener(this);
	asked_for_spin.setOnItemSelectedListener(this);
		
	
    }

	//private void method(TextView playerData)
	
	public void displayPlayerCards()
	{
		playerData.setText("Pn:" + "C:12?? "+  "D:1257 "+  "H:12?8 " + "S:12??" );
	}
	
	

    public void onNothingSelected(AdapterView<?> parent) {
        // Another interface callback
		playerData.setText( "test");
		
    }
	@Override
	public void onItemSelected(AdapterView<?> p1, View p2, int p3, long p4)
	{
		playerData.setText( Integer.toString(p3) + Long.toString(p4));
		

	}
}
