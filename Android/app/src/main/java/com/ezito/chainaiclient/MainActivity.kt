package com.ezito.chainaiclient

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        var curplayer = 1

        btn00.setOnClickListener({
            Toast.makeText(this, "DOU", Toast.LENGTH_LONG).show()
        })
    }

}
