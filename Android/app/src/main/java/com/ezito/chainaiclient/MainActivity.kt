package com.ezito.chainaiclient

import android.os.Build
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.os.Environment
import android.widget.Toast
import com.google.gson.Gson
import java.io.File
import kotlinx.android.synthetic.main.activity_main.*
import java.util.jar.Manifest

class MainActivity : AppCompatActivity() {
    val pathfold = File(Environment.getExternalStorageDirectory().absolutePath + "/ChainAI/")
    val tablero = File(pathfold, "tablero.json")
    object example {
        var cord = "00"
        var cordx = 0
        var cordy = 0
        var points = 0
        var max = 0
        var limx = 1
        var limy = 1
        var player = 0
    }
    val maxx = 5
    val maxy = 9
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
        var curx = 0
        var cury = 0
        pathfold.mkdirs()
        tablero.createNewFile()
        tablero.writeText("{ boxes :[")
        while (cury <= maxy) {
            while (curx <= maxx) {
                example.max = 0
                example.cordx = curx
                example.cordy = cury
                example.cord = curx.toString() + cury.toString()
                example.player = 0
                if (example.cordx == 0) {
                    example.limx = 1
                    example.max += 1
                } else if (example.cordx == maxx) {
                    example.limx = -1
                    example.max += 1
                }
                else {
                    example.limx = 2
                    example.max += 2
                }
                if (example.cordy == 0) {
                    example.limy = 1
                    example.max += 1
                } else if (example.cordy == maxy) {
                    example.limy = -1
                    example.max += 1
                }
                else {
                    example.limy = 2
                    example.max += 2
                }
                tablero.printWriter().use {out -> out.println(Gson().toJson(example).toString())}
                curx += 1
            }
            cury += 1
            curx = 0
        }
        tablero.appendText("] }")
        Toast.makeText(this, tablero.toString(), Toast.LENGTH_LONG).show()
        return true
    }
}
