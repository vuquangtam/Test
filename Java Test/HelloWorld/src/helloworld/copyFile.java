package helloworld;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.JOptionPane;
public class copyFile extends Frame implements ActionListener{
	Label blank = new Label();
	Label top_lbl = new Label("Form Copy");
	Label src_lbl = new Label("Source");
	Label dst_lbl = new Label("Destination");
	TextField src_tf = new TextField(10);
	TextField dst_tf = new TextField(10);
	Button copy_btn = new Button("Copy");
	Button cancel_btn = new Button("Cancel");
	copyFile(String title){
		super(title);
		setLayout(new GridLayout(4,2));
		copy_btn.addActionListener(this);
		cancel_btn.addActionListener(this);
		add(top_lbl);
		add(blank);
		add(src_lbl);
		add(src_tf);
		add(dst_lbl);
		add(dst_tf);
		add(copy_btn);
		add(cancel_btn);
		this.addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent ae){
				System.exit(0);
			}
		});
	}
	public void actionPerformed(ActionEvent ae){
		if(ae.getSource() == copy_btn){
			String text = copy(src_tf.getText(), dst_tf.getText());
			JOptionPane.showMessageDialog(copy_btn, text);
		}
		else if (ae.getSource() == cancel_btn) System.exit(0);
	}
	
	private String copy(String src, String dst){
		try{
			FileInputStream r = new FileInputStream(src);
			FileOutputStream w;
			try{
				w = new FileOutputStream(dst);

			}
			catch(IOException e){
				r.close();
				return"Cannot Create File in " + dst;
			}
			while(true){
				int ch = r.read();
				if(ch == -1) break;
				byte temp = (byte)(char)ch;
				w.write(temp);
			}
			w.close();
			r.close();
			return ("File copy successful\n" + src + " to " + dst);
		}
		catch(IOException e){
			return ("Cannot Open File in " + src);
		}
	}

	public static void main(String[] args){
		copyFile test = new copyFile("copy file");
		test.setSize(300,300);
		test.setVisible(true);
	}

}
