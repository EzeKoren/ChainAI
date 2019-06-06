package com.ezito.chainaiclient

import android.os.Build
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.os.Environment
import android.widget.Toast
import java.io.File
import kotlinx.android.synthetic.main.activity_main.*
import java.util.jar.Manifest

class MainActivity : AppCompatActivity() {
    val pathfold = File(Environment.getExternalStorageDirectory().absolutePath + "/ChainAI/")
    val tablero = File(pathfold, "tablero.json")
    var example = {
        var cord = "00"
        var cordx = 0
        var cordy = 0
        var points = 0
        var max = 0
        var limx = 1
        var limy = 1
        var player = "0"
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        Reset()
        var curplayer = 1
        btn00.setOnClickListener({
            Toast.makeText(this, "dou", Toast.LENGTH_LONG).show()
        })
    }



    fun Reset(): Boolean {
        pathfold.mkdirs()
        tablero.createNewFile()
        tablero.writeText("Hello world!")
        Toast.makeText(this, tablero.toString(), Toast.LENGTH_LONG).show()
        return true
    }
}
